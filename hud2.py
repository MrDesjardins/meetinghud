from deepface import DeepFace
models = ['VGG-Face', 'Facenet', 'OpenFace', 'DeepFace', 'DeepID', 'Dlib']
DeepFace.stream(db_path="C:/facial_db", model_name=models[1])
