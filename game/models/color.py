from colorama import Fore


class Color:

    @staticmethod
    def color_red(string: str) -> str:
        """
        Returns the input string with a red color.

        This function uses the 'colorama' module to add a red color to the input string. # noqa E501

        Args:
        word (str): A string to add color to.

        Returns:
        A string with a red color.
        """
        return Fore.RED + string + Fore.RESET

    @staticmethod
    def color_blue(string: str) -> str:
        """
        Returns the input string with a blue color.

        This function uses the 'colorama' module to add a blue color to the input string. # noqa E501

        Args:
        word (str): A string to add color to.

        Returns:
        A string with a blue color.
        """
        return Fore.BLUE + string + Fore.RESET

    @staticmethod
    def color_black(string: str) -> str:
        """
        Returns the input string with a black color.

        This function uses the 'colorama' module to add a black color to the input string. # noqa E501

        Args:
        word (str): A string to add color to.

        Returns:
        A string with a black color.
        """
        return Fore.BLACK + string + Fore.RESET

    @staticmethod
    def color_green(string: str) -> str:
        """
        Returns the input string with a green color.

        This function uses the 'colorama' module to add a green color to the input string. # noqa E501

        Args:
        word (str): A string to add color to.

        Returns:
        A string with a green color.
        """
        return Fore.GREEN + string + Fore.RESET

    @staticmethod
    def color_blue_light(string: str) -> str:
        """
        Returns the input string with a light blue color.

        This function uses the 'colorama' module to add a light blue color to the input string. # noqa E501

        Args:
        word (str): A string to add color to.

        Returns:
        A string with a light blue color.
        """
        return Fore.LIGHTBLUE_EX + string + Fore.RESET
