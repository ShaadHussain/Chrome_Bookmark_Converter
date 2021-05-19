import sys


print("Sys argv 0")
print(sys.argv[1])
print("Sys argv 1")
# print(sys.argv[2])



# orig_bkmks = open("bookmarks_5_15_21.html", "r")
# new_bkmks = open("new_bkmks.txt","a") #append mode

#Command should be:
# python3 bkmk_parser.py path_to_orig_bkmks_html path_to_file_to_convert_to
#  /Users/shaadhussain/Desktop/PersonalProjects/Bookmark_Parser/new_bkmks.txt
#
orig_bkmks = open(sys.argv[1], "r") #opening read mode
new_bkmks = open("new_bkmks.txt","a") #append mode


bkmk_ct = 1

for line in orig_bkmks:
    #Parsing titles
    sample = line[0:16]
    if "<DT><H3" in line:
        line = line.strip()
        line = line[9:]
        start_ind = line.find(">")
        end_ind = line.find("<")
        group_title = line[start_ind + 1:end_ind]

        new_bkmks.write(group_title + ":\n\n")
        bkmk_ct = 1        
        # print(line)

    #Parsing a link
    elif "<DT><A HREF" in line:
        line = line.strip()
        line = line[8:]
        start_ind = line.find("=")
        end_ind = line.find(" ")
        allig_ind1 = line.find(">")
        allig_ind2 = line.find("<")
        link_str = line[start_ind + 2 : end_ind - 1]
        name_str = line[allig_ind1 + 1 : allig_ind2]

        new_bkmks.write("\t" + str(bkmk_ct) + ". " + name_str + "\n")
        new_bkmks.write("\t\t" + link_str + "\n\n")

        bkmk_ct = bkmk_ct + 1