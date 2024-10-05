# Access cluster
ssh -i /home/simao/.ssh/id_rsa simaocunha71@login-hpc.lsd.di.uminho.pt

# Transfer data from local to the cluster (make sure to be on the folder to be transfered)
scp -r * simaocunha71@login-hpc.lsd.di.uminho.pt:/home/ldap/simaocunha71

# Transfer data from local to the cluster
scp llama-2-7b.Q2_K.gguf simaocunha71@login-hpc.lsd.di.uminho.pt:/home/ldap/simaocunha71/thesis_repository/llms/llama_c++/models

# Transfer data from the cluster to local
scp -r simaocunha71@login-hpc.lsd.di.uminho.pt:/home/ldap/simaocunha71 .
