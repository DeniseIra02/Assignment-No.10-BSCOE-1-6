import qrcode

with open('ctiDetails.txt') as cti_txt:
    raw_details = cti_txt.read()

qr = qrcode.make(raw_details)
qr.save('den_qrcode.png')