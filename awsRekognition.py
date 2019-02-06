
import boto3

if __name__ == "__main__":

    imageFile='/home/gokul/Pictures/roast.jpg'
    client=boto3.client('rekognition')
   
    with open(imageFile, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()}, Attributes = ["ALL"])
        
    print(response)

    print('Done...')
