from brownie import accounts, network, MockV3Aggregator 
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork-dev"]
LOCAL_DEVELOPMENT_ENVIROMENTS = ["development", "ganache-local"]

def get_account():
    if (network.show_active() in LOCAL_DEVELOPMENT_ENVIROMENTS 
    or network.show_active() in FORKED_LOCAL_ENVIROMENTS):
        return accounts[0]
    else:
        return accounts.load('test')

def  deploy_mocks():
    print(f"the active network is {network.show_active()}")
    print("activation Mocks....") 
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks deployed!")