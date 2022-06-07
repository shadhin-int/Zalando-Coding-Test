def solution(S, T):
    s = list(S)
    res_s = []
    for i in s:
        if i.isdigit():
            temp = ["*"] * int(i)
            res_s += temp
        else:
            res_s.append(i)

    t = list(T)
    res_t = []
    for i in t:
        if i.isdigit():
            temp = ["*"] * int(i)
            res_t += temp
        else:
            res_t.append(i)

    if len(res_s) != len(res_t):
        return False

    for i in range(len(res_s)):
        if res_s[i] == "*" or res_t[i] == "*":
            continue
        elif res_s[i] != res_t[i]:
            return False
    return True
