from numpy import sin, cos, linspace, zeros_like
from scipy.integrate import odeint
from pylab import plot, xlabel, ylabel, show

inic = [1., 0., 0., 0.,]

S=800
t = linspace(0, 100., S)

coup = 0.1
diss = 1

def f(z,time):
    return [ z[1], -z[0] - coup*z[2] ,
             z[3], -z[2] - coup*z[0] - diss*z[3]
           ]

res = odeint(f, inic, t)
plot(t, res[:,0],c='blue',lw=2)
plot(t, res[:,2],c='red',lw=2)

if True:
    x = zeros_like(t)
    y = zeros_like(t)
    for i in range(S):
        x[i] = cos(t[i]) + coup*coup/(2*diss)*(sin(t[i])-t[i]*cos(t[i]))
        y[i] = -coup/diss*sin(t[i])
    plot(t, x, c='cyan')
    plot(t, y, c='magenta')

xlabel('time')
ylabel('amplitude')

show()

