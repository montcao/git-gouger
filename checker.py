import importlib
import pkgutil
import checks

class GitGouger:
    def __init__(self, owner, repo, token=None):
        self.owner = owner
        self.repo = repo
        self.token = token
        self.headers = {"Authorization": f"token {token}"} if token else {}

    def load_checks(self):
        """Dynamically import all modules in checks/"""
        check_modules = []
        package = checks
        for _, name, _ in pkgutil.iter_modules(package.__path__):
            module = importlib.import_module(f"{package.__name__}.{name}")
            if hasattr(module, "run"):
                check_modules.append(module)
        return check_modules

    def run_checks(self):
        results = []
        for module in self.load_checks():
            try:
                res = module.run(self.owner, self.repo, self.headers)
                results.append(res)
            except Exception as e:
                print(f"Error: {e}")
        return results
