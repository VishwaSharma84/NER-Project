echo [$(date)]: "START"
echo [$(date)]: "creating environment"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate environment"
source activate ./env

echo [$(date)]: "install requirements"
pip install -r requirements.txt
# echo [$(date)]: "install pytorch dependency"
# pip install torch --extra-index-url https://download.pytorch.org/whl/cu113 -q
echo [$(date)]: "END"

# # to remove everything -
# # rm -rf env/ .gitignore conda.yaml README.md .git/