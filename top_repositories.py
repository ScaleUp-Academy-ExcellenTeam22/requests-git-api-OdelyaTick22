import requests


def top_repositories(language: str, number_of_repos: int) -> str:
    """
    A function that requests the top repositories from GitHub, by programming language,
    ordered by the number of stars each repository has.
    :param language: The programming language to filter by.
    :param number_of_repos: The number of repositories to return.
    :return: String of all top repositories from GitHub, by programming language,
    ordered by the number of stars each repository has.
    """
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
    response = requests.get(url)
    response_dict = response.json()
    repos_dicts = response_dict['items']
    result = ""
    for i in range(number_of_repos):
        repo_dict = repos_dicts[i]
        lang = language.capitalize()
        result += f"-> {repo_dict['name']} is a {lang} repo with {repo_dict['stargazers_count']} stars.\n"
    return result


if __name__ == "__main__":
    print(top_repositories("python", 20))
