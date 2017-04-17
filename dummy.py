from pymongo import MongoClient
client = MongoClient()


norm = ['H', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl']
lan = ['La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']
ac = ['Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']



client.Materials.Entropy.drop()
client.Materials.Gibsson.drop()

entropy_list = []
gibbson_list = []
for l in lan:
    for n in norm:
        for a in ac:
            for i in range(1, 5):
                ii = str(i)
                for j in range(1, 5):
                    jj = str(j)
                    for k in range(1, 5):
                        ele = {l: i, n: j, a: k}
                        formula = l+('' if i == 1 else ii) +n+('' if j == 1 else jj)+a+('' if k == 1 else str(k))
                        entropy_list.append({'_id': formula, 'ele': ele})
                        gibbson_list.append({'_id': formula, 'ele': ele})


client.Materials.Entropy.insert_many(entropy_list)
client.Materials.Gibsson.insert_many(entropy_list)
