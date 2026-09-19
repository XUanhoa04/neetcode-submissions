class Solution:
    def encode(self, strs: list[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Tìm vị trí của dấu '#' tiếp theo để lấy độ dài
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            # Lấy chuỗi con có độ dài 'length' ngay sau dấu '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Di chuyển con trỏ i đến vị trí chuỗi kế tiếp
            i = end
            
        return res