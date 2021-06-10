import matplotlib.pyplot as plt

dp = [0.041199999999999994, 0.04409999999999999, 0.06700000000000002, 0.028600000000000004, 0.08249999999999999, 0.1641]
bf = [0.37509999999999993, 0.09579999999999998, 0.6740999999999999, 0.0653, 2.5126, 0.1485]

print('here')
plt.ylabel('Tiempos promedio de ejecucion DP')
plt.xlabel('EXperimentos')
plt.plot(dp)
plt.show()


plt.ylabel('Tiempos promedio de ejecucion BF')
plt.xlabel('EXperimentos')
plt.plot(bf)
plt.show()

