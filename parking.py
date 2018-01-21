import urllib2, json, time, datetime
from tqdm import tqdm

outfile = open("outfile.txt", "a")

while True:
    
    outfile.write(str(datetime.datetime.today()) + " ")

    for lot in [80, 81, 82, 83, 84, 85]:

        p = urllib2.urlopen("https://streetsoncloud.com/parking/rest/occupancy/id/%s" % lot)
        s = p.read()
        s = s[s.find("(")+1:s.rfind(")")]
        j = json.loads(s)
        
        print j["results"][0]["location_name"],
        outfile.write(j["results"][0]["free_spaces"] + " ")
        print j["results"][0]["total_spaces"]

    outfile.write("\n")
    outfile.flush()
    
    for i in tqdm(range(60)):
        time.sleep(1)

