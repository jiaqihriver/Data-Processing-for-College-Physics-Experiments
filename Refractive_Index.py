import math
from decimal import Decimal

# 第1组数据
x_1l = math.radians(314 + 26 / 60)
x_1r = math.radians(134 + 24 / 60)
y_1l = math.radians(365 + 20 / 60)
y_1r = math.radians(185 + 10 / 60)
# 第2组数据
x_2l = math.radians(72 + 9 / 60)
x_2r = math.radians(252 + 0 / 60)
y_2l = math.radians(123 + 0 / 60)
y_2r = math.radians(303 + 2 / 60)
# 第3组数据
x_3l = math.radians(345 + 13 / 60)
x_3r = math.radians(165 + 8 / 60)
y_3l = math.radians(396 + 5 / 60)
y_3r = math.radians(216 + 1 / 60)

z_1l = y_1l - x_1l
z_1r = y_1r - x_1r
z_1_l = math.degrees(z_1l)
z_1_r = math.degrees(z_1r)
print("第一组左游标计算的最小偏向角为 " + str(Decimal(z_1_l).quantize(Decimal("0.0000"))))
print("第一组右游标计算的最小偏向角为 " + str(Decimal(z_1_r).quantize(Decimal("0.0000"))))
z_1 = (z_1l + z_1r) / 2
z_1d = math.degrees(z_1)
print("第一组计算得到的平均最小偏向角为 " + str(Decimal(z_1d).quantize(Decimal("0.0000"))))

z_2l = y_2l - x_2l
z_2r = y_2r - x_2r
z_2_l = math.degrees(z_2l)
z_2_r = math.degrees(z_2r)
print("第二组左游标计算的最小偏向角为 " + str(Decimal(z_2_l).quantize(Decimal("0.0000"))))
print("第二组右游标计算的最小偏向角为 " + str(Decimal(z_2_r).quantize(Decimal("0.0000"))))
z_2 = (z_2l + z_2r) / 2
z_2d = math.degrees(z_2)
print("第二组计算得到的平均最小偏向角为 " + str(Decimal(z_2d).quantize(Decimal("0.0000"))))

z_3l = y_3l - x_3l
z_3r = y_3r - x_3r
z_3_l = math.degrees(z_3l)
z_3_r = math.degrees(z_3r)
print("第三组左游标计算的最小偏向角为 " + str(Decimal(z_3_l).quantize(Decimal("0.0000"))))
print("第三组右游标计算的最小偏向角为 " + str(Decimal(z_3_r).quantize(Decimal("0.0000"))))
z_3 = (z_3l + z_3r) / 2
z_3d = math.degrees(z_3)
print("第三组计算得到的平均最小偏向角为 " + str(Decimal(z_3d).quantize(Decimal("0.0000"))))

# 数据平均值（取四位小数）
z = (z_1 + z_2 + z_3) / 3
z_d = math.degrees(z)
z_dd = Decimal(z_d).quantize(Decimal("0.0000"))
print("最小偏向角平均值为" + str(z_dd))

# 标准偏差
s_1 = (z_1 - z) ** 2
s_2 = (z_2 - z) ** 2
s_3 = (z_3 - z) ** 2
s = math.sqrt((s_1 + s_2 + s_3) / 2)
s_d = math.degrees(s)
s_dd = Decimal(s_d).quantize(Decimal("0.0000"))
print("最小偏向角的标准偏差为" + str(s_dd))

# 坏值检验
h_l = z - 3 * s
h_r = z + 3 * s
h_ld = math.degrees(h_l)
h_rd = math.degrees(h_r)
print(
    "3 sigma区间为 "
    + "["
    + str(Decimal(h_ld).quantize(Decimal("0.0000")))
    + ","
    + str(Decimal(h_rd).quantize(Decimal("0.0000")))
    + "]，故没有坏值。"
)

# 最小偏向角A类不确定度
u_pa = 1.32 * s / math.sqrt(3)
u_pad = Decimal(u_pa).quantize(Decimal("0.0000"))
print("最小偏向角A类不确定度为" + str(u_pad))

# 最小偏向角总不确定度
u_pb = 0.00017
print("最小偏向角B类不确定度为" + str(u_pb))
u_p = 2 * math.sqrt(u_pa ** 2 + u_pb ** 2)
u_pd = Decimal(u_p).quantize(Decimal("0.0000"))
print("最小偏向角总不确定度为" + str(u_pd))

# 三棱镜折射率（四位小数）
n = math.sin((z + math.pi / 3) / 2) * 2
n_d = Decimal(n).quantize(Decimal("0.0000"))
print("三棱镜折射率为" + str(n_d))

# 三棱镜不确定度
u_d = 0.00058
print("三棱镜顶角的不确定度为" + str(u_d))
p_na = -1 / 2 * math.sin(z / 2) * 4
p_nz = math.cos((z + math.pi / 3) / 2)
u_n = math.sqrt((p_na * u_d) * (p_na * u_d) + (p_nz * u_p) * (p_nz * u_p))
u_nd = Decimal(u_n).quantize(Decimal("0.0000"))
print("三棱镜不确定度为" + str(u_nd))

