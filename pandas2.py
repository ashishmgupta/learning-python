cols = ["first_seen_utc","sha256_hash","md5_hash","sha1_hash","reporter","file_name","file_type_guess","mime_type","signature","clamav","vtpercent","imphash","ssdeep","tlsh"
]

# skip cert number of lines till you get the actual data with ignoring the lines which may error out
df_malware_bazaar = pd.read_csv("malware_bazaar.csv", skiprows=9, on_bad_lines="warn", names=cols)

# Stats count descending by signature column 
df_malware_bazaar.groupby("sigrature").size().sort_values(ascending=True)

# top 10 
df_malware_bazaar[df_malware_bazaar["signature"]=="mirai"].sort_values(ascending=False).head(10)



import requests

def getStatusForUrl(url):
	resp = requests.get(url)
	return rest.status_code
	
	
all_lines = []
with open("url.csv","r") as f:
	all_lines = f.readlines()

for line in all_lines:
	# skip the header
    if not all_lines.index(line)==0:
        url_only = line.split(",")[1].replace("\n","")
        print(url_only)
        print(getStatusForUrl(url_only))
		
