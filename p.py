list=[0,0.008,0.033,0.068,0.124,0.198,0.282,0.385,0.502,0.632,0.782]
prompt=int(input("here:"))
d1=list[prompt-1]
d2=list[prompt+1]
res=(0.5*0.024*((d2-d1)/0.08)*((d2-d1)/0.08))
print(res)
import matplotlib.pypilot as plt
%matplotlib inline
x=[0,0.04,0.08,0.12,0.16,0.2,0.24,0.24,0.28,0.32,0.36,0.4]
y=[0,0.002,0.00675,0.015,0.0316,0.468,0.0655,0.0907,0.114,0.147]
plt.plot(x,y)
