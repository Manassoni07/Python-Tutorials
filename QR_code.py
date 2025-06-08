import qrcode

img = qr.make("https://www.youtube.com/watch?v=JgDNFQ2RaLQ&list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbAVMJgDNFQ2RaLQ&start_radio=1")
img = qr.save("qr1.png")