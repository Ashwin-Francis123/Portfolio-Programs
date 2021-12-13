import webbrowser
import time
import sys

print("\nI would suggest using commas to specify where the place is for better clarity.")
print("e.g. Los Angeles, California, America")
place = input("Place: ")
print("\n")
webbrowser.open("https://www.google.com/maps/search/" + place)
#Loading Bar
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
for i in progressbar(range(15), "Searching: ", 40):
    time.sleep(0.1)
