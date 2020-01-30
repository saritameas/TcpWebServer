import argparse
import requests

# Uses standard library to parse integer argument
parser = argparse.ArgumentParser(description='Calculate factorial')
parser.add_argument('integer', type=int,
                    help='an integer to be calculated')

args = parser.parse_args()

if __name__ == "__main__":
    # Calls server to calculate factorial and returns value in HTTP response
    resp = requests.get('http://localhost:8888/{}'.format(args.integer))
    print resp.content
