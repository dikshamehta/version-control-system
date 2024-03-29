""" Display the commits from the latest commit to the first commit """
import util
from io_util import print_yellow, print_red, print_green


def print_commit_log(commit_obj, commit_hash):
    print_yellow("LOG:" + commit_hash)
    print_green("tree:" + commit_obj["tree"])
    try:
        print_green("parent:" + commit_obj["parent"])
    except KeyError:
        pass
    print_green("author:" + commit_obj["author"])
    print_green("committer:" + commit_obj["committer"])
    print_green("message:" + commit_obj["message"] + "\n")


def log_util(commit_hash):
    if commit_hash == "":
        return

    commit_obj = util.decompress_commit(commit_hash)
    # with open(os.path.join(OBJ_DIR, commit_hash), "rb") as f:
    #     commit_obj = f.read()
    #     commit_obj = zlib.decompress(commit_obj)
    #     commit_obj = pickle.loads(commit_obj)
    #
    print_commit_log(commit_obj, commit_hash)

    try:
        commit_hash = commit_obj["parent"]
        log_util(commit_hash)
    except KeyError:
        pass


def log():
    # with open(HEAD_PATH) as head_file:
    #     head = head_file.read()
    #
    # with open(os.path.join(BRANCH_DIR, head)) as branch_file:
    #     commit_hash = branch_file.read()

    print_yellow("Head:" + util.get_head_content() + "\n")

    commit_hash = util.get_last_commit_hash()

    log_util(commit_hash)

# if __name__ == '__main__':
#     log()
