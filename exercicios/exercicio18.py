"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
 calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho= float (input('qual o tamanho do arquivo para dowload?:')) 
velocidade= float (input('qual a velocidade de sua internet?:')) 

print (f' irá demorar {tamanho/velocidade:.0f} minutos para finalizar o dowload do arquivo')