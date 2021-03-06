"""Uploads a file to GCS.

Usage: python3 gcs_upload.py <src> <dst>.
"""

from Crypto.Cipher import AES
from google.cloud import storage

import base64
import os
import sys
import tempfile

IV = base64.b64decode("tMNoHB8UYUlyWAdONqR0Sw==")
KEY = base64.b64decode(os.getenv("GCS_ENCRYPTION_KEY_B64"))

# service key json encrypted using AES-256-CBC
SERVICE_JSON_ENCRYPTED = base64.b64decode("""
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
""")


def CallWithFile(func, data):
  """Calls func("/path/to/tempfile/containing/data")."""
  tmp_file = tempfile.NamedTemporaryFile(delete=False)
  try:
    tmp_file.write(data)
    tmp_file.close()
    return func(tmp_file.name)
  finally:
    os.remove(tmp_file.name)


def main(argv):
  cipher = AES.new(KEY, AES.MODE_CBC, IV)
  service_json = cipher.decrypt(SERVICE_JSON_ENCRYPTED)
  gcs_client = CallWithFile(storage.Client.from_service_account_json,
                            service_json)
  gcs_bucket = gcs_client.bucket("autobuilds-fleetspeak")
  gcs_blob = gcs_bucket.blob(argv[2])
  gcs_blob.upload_from_filename(argv[1])


if __name__ == "__main__":
  main(sys.argv)
