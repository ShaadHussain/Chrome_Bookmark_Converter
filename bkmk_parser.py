orig_bkmks = open("bookmarks_5_15_21.html", "r")
# orig_bkmks = open("bkmks_ex.html", "r")
new_bkmks = open("new_bkmks.txt","a") #append mode


line2 = orig_bkmks.readline()
print("Line 2")
print(line2)

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
        # print(line)
