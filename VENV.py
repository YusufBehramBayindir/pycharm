###############################################
# Virtual Environment (Sanal Ortam)  ve (Package Managment) Paket Yönetimi
###############################################

# Sanal ortamların listelenmesi:
# conda env list


# Sanal ortam oluşturma
# conda create -n ybb_env
# conda create -n ybb_env python=3.4


# Sanal ortamı aktif etme
# conda activate ybb_env


# Yüklü paketlerin listelenmesi
# conda list


# Paket yükleme:
# conda install numpy


# Aynı anda birden fazla paket yükleme:
# conda install numpy scipy pandas


# Paket silme:
# conda remove package_name

# Belirli bir versiyonuna göre paket yükleme:
# conda install numpy=1.20.1

# Paket yükseltme:
# conda upgrade conda

# Exporting the environment file
# conda env export > environment.yml

# Deaktive etmek:
# conda deactivate

# Remove env
# conda env remove -n myenv

# update conda by running
# conda update -n base -c defaults conda
