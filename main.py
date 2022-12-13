import qrcode
import sys

def main():
  if len(sys.argv) < 3:
    sys.exit('Please enter a valid arguments. Example: python main.py "url" "file_name"')
  else:
    url = sys.argv[1]
    file_name = sys.argv[2]
  qr = qrcode.QRCode(version=1, border=0)
  qr.add_data(url)
  qr.make(fit=True)
  img = qr.make_image(fill_color="white", back_color="transparent")
  img.save(f'{file_name}.png')

if __name__=="__main__":
  main()
