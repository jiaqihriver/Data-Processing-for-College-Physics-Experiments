import math
from decimal import Decimal

# 记录单缝到功率计探头的距离z，单位（cm）
z_1 = 78.45
z_2 = 78.48
z_3 = 78.47

# 记录单缝衍射3级暗条纹间距测量数据，单位（mm）
x_3l = 42.700  # 左侧3级暗条纹位置
x_3r = 58.600  # 友侧3级暗条纹位置
o = 50.600  # 中心位置

# 计算z的平均值
z = (z_1 + z_2 + z_3) / 3
z_d = Decimal(z).quantize(Decimal("0.00"))
print("单缝到功率计探头的距离z为", str(z_d), "cm")

# z的标准偏差
s_z1 = (z_1 - z) ** 2
s_z2 = (z_2 - z) ** 2
s_z3 = (z_3 - z) ** 2
s_z = math.sqrt((s_z1 + s_z2 + s_z3) / 2)
s_zd = Decimal(s_z).quantize(Decimal("0.00"))
print("z的标准偏差为", str(s_zd), "cm")

# z的坏值检验
h_l = z - 3 * s_z
h_r = z + 3 * s_z
print(
    "3 sigma区间为 "
    + "["
    + str(Decimal(h_l).quantize(Decimal("0.00")))
    + ","
    + str(Decimal(h_r).quantize(Decimal("0.00")))
    + "]，故没有坏值。"
)

# z的不确定度（保留两位小数 ）
u_za = 1.32 * s_z / math.sqrt(3)
print("z的A类不确定度为 ", str(Decimal(u_za).quantize(Decimal("0.000"))), "cm")
u_zb = 0.005 / math.sqrt(3)
print("z的B类不确定度为 ", str(Decimal(u_zb).quantize(Decimal("0.000"))), "cm")
u_z = 2 * math.sqrt(u_za ** 2 + u_zb ** 2)
print("z的总不确定度为 ", str(Decimal(u_z).quantize(Decimal("0.000"))), "cm")

# 计算3级暗条纹与中心位置平均的距离
x_l = o - x_3l
x_r = x_3r - o
print("左侧3级暗条纹与中心位置的距离为", str(Decimal(x_l).quantize(Decimal("0.000"))), "mm")
print("右侧3级暗条纹与中心位置的距离为", str(Decimal(x_r).quantize(Decimal("0.000"))), "mm")
x = (x_l + x_r) / 2
print("3级暗条纹与中心位置平均的距离为", str(Decimal(x).quantize(Decimal("0.000"))), "mm")

# x_k的标准偏差
s_xl = (x_l - x) * (x_l - x)
s_xr = (x_r - x) * (x_r - x)
s_x = math.sqrt(s_xl + s_xr)
print("x_k的标准偏差为", str(Decimal(s_x).quantize(Decimal("0.000"))), "mm")

# x_k的坏值检验
h_xl = x - 3 * s_x
h_xr = x + 3 * s_x
print(
    "3 sigma区间为 "
    + "["
    + str(Decimal(h_xl).quantize(Decimal("0.000")))
    + ","
    + str(Decimal(h_xr).quantize(Decimal("0.000")))
    + "]，故没有坏值。"
)

# x_k的不确定度
u_xa = 1.84 * s_x / math.sqrt(2)
print("x_k的A类不确定度为 ", str(Decimal(u_xa).quantize(Decimal("0.000"))), "mm")
u_xb = 0.004 / math.sqrt(3)
print("x_k的B类不确定度为 ", str(Decimal(u_xb).quantize(Decimal("0.000"))), "mm")
u_x = 2 * math.sqrt(u_xa ** 2 + u_xb ** 2)
print("x_k的总不确定度为 ", str(Decimal(u_x).quantize(Decimal("0.000"))), "mm")

# 光波长(nm)、百分比差及其不确定度(保留整数)
wl = 0.20 * x / 3 / z / 10
wln = wl * 1000000
print("入射光波长为", str(Decimal(wln).quantize(Decimal("0."))), "nm")
p = abs((wln - 650) / 650) * 100
print("百分差为", str(Decimal(p).quantize(Decimal("0.0"))), "%")

u_wl = math.sqrt((u_x / x) ** 2 + (u_z / z) ** 2) * wl
u_wln = u_wl * 1000000
print("入射光波长的不确定度为", str(Decimal(u_wln).quantize(Decimal("0."))), "nm")

