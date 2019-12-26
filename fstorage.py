import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/manthanmkulakarni/Desktop/fitness-eb2f668d6532.json"
# Enable Storage

cred = credentials.Certificate('/Users/manthanmkulakarni/Desktop/fitness-eb2f668d6532.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'fitness-e0935.appspot.com'
})

bucket = storage.bucket()
uploadBlob = bucket.blob('photos/Diamond-face-shape-bespke-unit-Bordered.png')
uploadBlob.upload_from_filename(filename='/Users/manthanmkulakarni/Downloads/Diamond-face-shape-bespke-unit-Bordered.png')


downloadBlob=bucket.blob('photos/Diamond-face-shape-bespke-unit-Bordered.png')
with open("Diamond-face-shape-bespke-unit-Bordered.png", "wb") as file_obj:
    downloadBlob.download_to_file(file_obj)

