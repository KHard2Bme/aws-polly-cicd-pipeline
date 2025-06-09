import os
import boto3

def synthesize_speech(text, output_filename):
    # Initialize Polly client
    polly = boto3.client('polly')

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'  
    )

    # Save the audio stream to a file
    with open(output_filename, 'wb') as file:
        file.write(response['AudioStream'].read())

    print(f"Generated audio: {output_filename}")


def upload_to_s3(file_path, bucket_name, object_key):
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Upload file to S3
    s3.upload_file(file_path, bucket_name, object_key)
    print(f"Uploaded to s3://{bucket_name}/{object_key}")


def main():
    # Load environment variables
    bucket_name = os.environ.get('S3_BUCKET_NAME')
    output_filename = os.environ.get('OUTPUT_FILENAME', 'output.mp3')
    object_key = f'polly-audio/{output_filename}'

    # Read the input text
    with open('speech.txt', 'r') as file:
        text = file.read()

    # Generate speech
    synthesize_speech(text, output_filename)

    # Upload to S3
    upload_to_s3(output_filename, bucket_name, object_key)


if __name__ == '__main__':
    main()

