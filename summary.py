import os.path

def search(sum_file : str = 'sum', folder : str = '', boundaries : tuple = (3, 4), out : str = 'res.txt'):

    with open(sum_file, 'r') as f:
        mols = f.read().split('\n')
        f.close()

    res={}

    for mol in mols:
        with open(os.path.join(folder, mol), 'r') as f:
            energies = f.read().split('\n')
            f.close()
        levels = {}
        for energy in energies:
            energy = energy.split(' ')
            if 'HOMO' in energy:
                levels['HOMO'] = float(energy[1])
                levels['HOMO_pos'] = int(energy[0])
            elif 'LUMO' in energy:
                levels['LUMO'] = float(energy[1])
            levels[int(energy[0])] = float(energy[1])
        levels['H->L'] = levels['LUMO']-levels['HOMO']
        res[mol] = levels

    with open(out, 'w') as f:
        test_res = []
        for mol in mols:
            levels = res[mol]
            done = []
            for level_A in levels:
                if type(level_A) is not int:
                    continue
                for level_B in levels:
                    if type(level_B) is not int:
                        continue
                    done.append((level_A, level_B))
                    if boundaries[0] <= abs(levels[level_A]-levels[level_B]) <= boundaries[1] and (level_B, level_A) not in done:
                        homo_1 = level_B-levels['HOMO_pos']
                        if homo_1 == 0:
                            homo_1 = 'HOMO'
                        elif homo_1 == 1:
                            homo_1 = 'LUMO'
                        elif homo_1 > 1:
                            homo_1 = f'LUMO+{homo_1-1}'
                        elif homo_1<0:
                            homo_1 = f'HOMO{homo_1}'
                        homo_2 = level_A-levels['HOMO_pos']
                        if homo_2 == 0:
                            homo_2 = 'HOMO'
                        elif homo_2 == 1:
                            homo_2 = 'LUMO'
                        elif homo_2 > 1:
                            homo_2 = f'LUMO+{homo_2-1}'
                        elif homo_2<0:
                            homo_2 = f'HOMO{homo_2}'
                        test_res.append((f"{mol}: {homo_2} -> {homo_1} = {abs(levels[level_A]-levels[level_B])}", abs(levels[level_A]-levels[level_B])))
        
        test_res = sorted(test_res, key=lambda x: x[1])
        f.write('\n'.join([i[0] for i in test_res]))
        f.close()
        for line in [i[0] for i in test_res]: print(line)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        args = [3, 4]
    else:
        args = sys.argv[1:]
    search(boundaries=(float(args[0]), float(args[1])))
