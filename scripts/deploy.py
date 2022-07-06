from brownie import FundMe, config, accounts, network, MockV3Aggregator
from scripts.helpful_scripts import deploy_mocks, get_account, LOCAL_DEVELOPMENT_ENVIROMENTS
from scripts.fund_and_withdraw import fund

def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_DEVELOPMENT_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ] 
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    print(f"contract deploy to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()