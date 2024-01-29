import qrcode
import datetime
 
def main(data, image_filename, *args, **kwargs):
	if data is None or image_filename is None:
		raise ValueError("No data or image filename is provided. Please try again.")
	
	img = qrcode.make(data)
	img.save(image_filename + '.jpg')

if __name__ == '__main__':
	print('QR code generator...')
	
	data = input("What's the data to be encoded? (Website URL, Google search, UID, string, SHA-256 code or any string)\n")
	image_filename = input("How do you want to call the output? (Press Enter to choose default option)\n")
	if len(image_filename) == 0:
		image_filename = str(datetime.datetime.now().strftime('%d-%m-%y_%H:%M:%S'))
	
	main(data, image_filename)
