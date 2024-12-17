import re


def break_after_matching(fp, regular_expression):
    # keep reading lines and include line with matchin regex
    lines = []
    line = fp.readline()
    while line:
        lines.append(line)
        if re.match(regular_expression, line):
            yield lines
            lines = []
        line = fp.readline()


def main():
    # break by Monday Tuesday Wednesday Thursday Friday
    path = ""
    version = "v2"
    filename = path + "xpert_connect_" + version + ".txt"
    fileout = path + "xpert_connect_" + version + ".csv"
    regular_expression = r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"
    with open(filename) as fp:
        with open(fileout, "w") as fo:
            for x in break_after_matching(fp, regular_expression):

                # get rid of registered information
                if re.match(r"Registered", x[0]):
                    x.pop(0)

                # if job description is consuming two lines
                # join them
                if re.match(r"[^\n]", x[1]) and re.match("[^\n]", x[2]):
                    x[1] = x[1].strip() + " " + x[2]
                    x.pop(2)

                # if there is no job description add an empty one
                if re.match(r"\n", x[1]):
                    x.insert(1, "\n")

                # Remove the third and fourth ones
                x.pop(2)
                x.pop(2)

                # Break up the date
                _, date_time = x[4].split("**")
                adate, time_range = date_time.split(", ")
                from_time, to_time = time_range.split(" - ")
                x[4] = adate
                x.append(from_time)
                x.append(to_time)
                y = [k.strip() for k in x]
                fo.write("\t".join(y))
                fo.write("\n")


if __name__ == "__main__":
    main()
