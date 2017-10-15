import base64, sys, binascii, urllib

if len(sys.argv) != 3:
	sys.stderr.write('Usage ./dencode.py -e or -d string \n')
	sys.exit(1)

choice = sys.argv[1].split("-")[1].strip()
string = sys.argv[2].strip()

megan35 = "3GHIJKLMNOPQRSTUb=cdefghijklmnopWXYZ/12+406789VaqrstuvwxyzABCDEF5"
atom128 = "/128GhIoPQROSTeUbADfgHijKLM+n0pFWXY456xyzB7=39VaqrstJklmNuZvwcdEC"
zong22 = "ZKj9n+yf0wDVX1s/5YbdxSo=ILaUpPBCHg8uvNO4klm6iJGhQ7eFrWczAMEq3RTt2"
hazz15 = "HNO4klm6ij9n+J2hyf0gzA8uvwDEq3X1Q7ZKeFrWcVTts/MRGYbdxSo=ILaUpPBC5"
base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

class B64VariantEncoder:
    def __init__(self, translation):
        base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        self.lookup = dict(zip(base, translation))
        self.revlookup = dict(zip(translation, base))

    def encode(self, string):
        global lookup
        b64 = base64.b64encode(string)
        result = "".join([self.lookup[x] for x in b64])
        return result

    def decode(self, code):
        global revlookup
        b64 = "".join([self.revlookup[x] for x in code])
        result = base64.b64decode(b64)
        return result    

def encode(variant, string):
    encoder = B64VariantEncoder(variant)
    return encoder.encode(string)

def decode(variant, code):
    try:
        encoder = B64VariantEncoder(variant)
        return encoder.decode(code)
    except KeyError:
        return "no valid encoding"
    except TypeError:
        return "no correct padding"

if choice == "d":
	try:
		print("[ ]BASE64: "+ base64.b64decode(string).strip())
	except Exception as e:
		print("[ ]BASE64: "+str(e))
	try:
		print("[ ]BASE32: "+ base64.b32decode(string).strip())
	except Exception as e:
		print("[ ]BASE32: "+str(e))
	try:
		print("[ ]BASE16/HEX: "+ string.decode("hex"))
	except Exception as e:
		print("[ ]BASE16: "+str(e))
	try:
		print("[ ]BINARY: "+''.join(chr(int(string[i*8:i*8+8],2)) for i in range(len(string)//8)))
	except Exception as e:
		print("[ ]BINARY: "+str(e))
	try:
		print("[ ]ATOM128: "+ decode(atom128, string).strip())
	except Exception as e:
		print("[ ]ATOM128: "+str(e))
	try:
		print("[ ]MEGAN35: "+ decode(megan35, string).strip())
	except Exception as e:
		print("[ ]MEGAN35: "+str(e))
	try:
		print("[ ]HAZZ15: "+ decode(hazz15, string).strip())
	except Exception as e:
		print("[ ]HAZZ15: "+str(e))
	try:
		print("[ ]ZONG22: "+ decode(zong22, string).strip())
	except Exception as e:
		print("[ ]ZONG22: "+str(e))
	try:
		url=string
		decoded_url=urllib.unquote(string).decode('utf8')
		i=-1
		while url != decoded_url:
			i+=1
			decoded_url=url
			url=urllib.unquote(decoded_url).decode('utf8')
		if i==-1:
			print("[ ]URL: Not a URL or Nothing to Decode")
		else:
			print("[ ]URL:Decoded "+str(i)+": "+decoded_url.strip())
	except Exception as e:
		print("[ ]URL: "+str(e))
	try:
		l=string.split(",")
		if len(l)>1:
			print("[ ]ASCII: "+''.join(chr(int(i)) for i in l))
	except Exception as e:
		print("[ ]ASCII: "+str(e))

elif choice=="e":
	try:
		print("[ ]BASE64: "+ base64.b64encode(string).strip())
	except Exception as e:
		print("[ ]BASE64: "+str(e))
	try:
		print("[ ]BASE32: "+ base64.b32encode(string).strip())
	except Exception as e:
		print("[ ]BASE32: "+str(e))
	try:
		print("[ ]BASE16/HEX: "+ string.encode("hex"))
	except Exception as e:
		print("[ ]BASE16: "+str(e))
	try:
		l=[ord(c) for c in string]
		print ("[ ]ASCII: "+str(l))
	except Exception as e:
		print("[ ]ASCII: "+str(e))
	try:
		print("[ ]ATOM128: "+ encode(atom128,string).strip())
	except Exception as e:
		print("[ ]ATOM128: "+str(e))
	try:
		print("[ ]MEGAN35: "+ encode(megan35,string).strip())
	except Exception as e:
		print("[ ]MEGAN35: "+str(e))
	try:
		print("[ ]HAZZ15: "+ encode(hazz15,string).strip())
	except Exception as e:
		print("[ ]HAZZ15: "+str(e))
	try:
		print("[ ]ZONG22: "+ encode(zong22,string).strip())
	except Exception as e:
		print("[ ]ZONG22: "+str(e))
	try:
		print ("[ ]URL: "+ urllib.quote_plus(string))
	except Exception as e:
		print ("[ ]URL: " + str(e))
	try:
		print ("[ ]BINARY: "+ ' '.join(format(ord(x), 'b') for x in string))
	except Exception as e:
		print ("[ ]URL: " + str(e))
else:
	sys.stderr.write('Usage ./dencode.py -e or -d string \n')
	sys.exit(1)