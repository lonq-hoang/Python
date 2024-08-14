#Đổi tiền từ USD sang VND
print("Nhập USD: ")
usd = float(input())
vnd = usd * 22

print(str(usd) + " USD = " + str(vnd) + "k VND")

#Đổi tiền từ VND sang USD
print("Nhập VND: ")
vnd = float(input())
usd = vnd / 22

print(str(vnd) + "k VND = " + str(usd) + " USD")