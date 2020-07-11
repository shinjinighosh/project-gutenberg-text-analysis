# a collection of helper functions to make quick latex code


def makeTopWordsTable(list):
    '''given an even length list of [word, frequency] pairs, create a two-columned latex table'''
    table_code = """\\begin{table}[h]\
                    \\centering\
                    \\begin{tabular}{c|l|r||c|l|r}\
                    \\toprule\
                    No. & Word & Count & No. & Word & Count \\\\\
                    \\midrule """
    i = 0
    top_half = len(list) // 2
    for i in range(top_half):
        table_code += str(i + 1) + " & " + list[i][0] + " & " + str(list[i][1]) + " & " + str(
            i + top_half + 1) + " & " + list[i + top_half][0] + " & " + str(list[i + top_half][1]) + " \\\\        "
    table_code += """\\bottomrule \
                        \\end{tabular}\
                        \\end{table}"""
    return table_code


# list = [["hi", 1], ["test", 2]]
# print(makeTopWordsTable(list))
