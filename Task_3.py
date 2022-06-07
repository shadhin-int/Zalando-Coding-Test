def Solution(self, S: str) -> str:
    dp = [0] * len(S)

    for i in range(1, len(S)):
        j = dp[i-1]
        while j > 0 and S[j] != S[i]:
            j = dp[j-1]
        if S[j] == S[i]:
            dp[i] = j+1

    return S[len(S)-dp[-1]:]
