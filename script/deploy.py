from src import ERC1967, counter_one, counter_two
import boa
import warnings


def deploy():
    implementation = counter_one.deploy()
    proxy = ERC1967.deploy(implementation.address, boa.env.eoa)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        proxy_with_abi = counter_one.at(proxy.address)
    proxy_with_abi.set_number(42)
    proxy_with_abi.set_number_two(77)

    print("Implementation 1")
    print(proxy_with_abi.number())
    print(proxy_with_abi.number_two())
    print(proxy_with_abi.version())
    # print("Balance: ", proxy_with_abi.balanceOf())
    print(implementation.number())

    # Upgrading
    implementation_two = counter_two.deploy()
    proxy.upgrade_to(implementation_two.address)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        proxy_with_abi = counter_two.at(proxy.address)
        # proxy_with_abi.set_message("Hello again!")
    print("Implementation 2")
    print(proxy_with_abi.number())
    print(proxy_with_abi.number_two())
    # print(proxy_with_abi.message())

    proxy_with_abi.decrement()
    print(proxy_with_abi.number())
    print(proxy_with_abi.number_two())

    print(proxy_with_abi.version())
    # print("Balance: ", proxy_with_abi.balanceOf())
    print(implementation_two.number())


def moccasin_main():
    deploy()
