def escada(N,M,matriz):
    result = 'S'
    first_not_zero = None
    only_zero = False
    for r in matriz:
        chars = [int(c) for c in r]

        if only_zero:
            if any(chars):
                result = 'N'
                break

        if first_not_zero is not None:
            if chars[first_not_zero]:
                result = 'N'
                break
            elif first_not_zero > 0 and any(chars[:first_not_zero]):
                result = 'N'
                break

        if any(chars):
            for y in range(0, len(chars)):
                if chars[y]:
                    first_not_zero = y
                    break
        else:
            only_zero = True
    return result