
# 93. Restore IP Addresses
# https://leetcode.com/problems/restore-ip-addresses


"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:
1 <= s.length <= 20
s consists of digits only.
"""


def solution_one(s:str) -> list[str]:
    if len(s) < 4 or len(s) > 12:
        return []
    
    valid_ips = []
    for dot_1_idx in range(1, len(s)-2):
        for dot_2_idx in range(dot_1_idx+1, len(s)-1):
            for dot_3_idx in range(dot_2_idx+1, len(s)):

                valid_ip = True
                parts = [s[:dot_1_idx], s[dot_1_idx:dot_2_idx], s[dot_2_idx:dot_3_idx:], s[dot_3_idx:]]
                for part in parts:
                    if len(part) > 1 and part[0] == "0":
                        valid_ip = False
                        break
                    part = int(part)
                    if part < 0 or part > 255:
                        valid_ip = False
                        break
                if valid_ip:
                    valid_ips.append(".".join(parts))

    return valid_ips


print(solution_one("25525511135"))
print(solution_one("0000"))
print(solution_one("101023"))
