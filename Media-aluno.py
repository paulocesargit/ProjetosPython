notas = [
    [8.5, 7.0, 9.5],  
    [6.0, 7.5, 8.0], 
    [9.0, 8.5, 10.0], 
    [7.0, 6.5, 8.0],  
]

soma_medias = 0

for aluno_notas in notas:
    media = sum(aluno_notas) / len(aluno_notas)  
    soma_medias += media  

print(f"Soma das médias dos alunos: {soma_medias:.2f}")