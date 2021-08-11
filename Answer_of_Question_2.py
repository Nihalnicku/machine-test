class Owners:

    def group_by_owners(files):
        valu = (list(files.values()))

        val = list(set(valu))
        keyst = (list(files.keys()))
        result = {}
        for i in range(len(val)):
            for j in range(len(keyst)):
                if val[i]==valu[j]:
                    emptylist = [keyst[j]]

                    if val[i] in result:

                        result[val[i]].append(keyst[j])

                    else:
                        result[val[i]] = emptylist


        return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(Owners.group_by_owners(files))