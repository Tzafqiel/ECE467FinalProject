import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

T = np.array([10,30,60,100])
power = np.array([0.58839, 1.72174, 3.51392, 3.53418])

# 300 represents number of points to make between T.min and T.max
xnew = np.linspace(T.min(), T.max(), 300) 

spl = make_interp_spline(T, power, k=3)  # type: BSpline
power_smooth = spl(xnew)
plt.title("Inverter Rise Time vs. Capacitance")
plt.xlabel("Capacitance femto farads")
plt.ylabel("Rise Time in nano seconds")
plt.plot(xnew, power_smooth)
plt.savefig("risetime_v_capacitance.png")