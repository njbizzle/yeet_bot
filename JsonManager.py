import json

def read_json(json_path, guild_id = None):
    with open(json_path, "r") as data:
        loaded_data = json.load(data)

        if guild_id: # if a guild id is given, then return info on the guild
            return loaded_data["guild_ids"][guild_id]

        return loaded_data


def write_json(json_path, data):
    with open(json_path, "w") as file:
        return json.dump(data, file, indent=2)

# ----- test_json.json -----
TEST_JSON_PATH = "test_json.json"

# ----- blank info constants -----
MEMBER_INFO_BLANK = {
    "member_value": 0,
    "member_saved_words": []
}

GUILD_INFO_BLANK = {
    "members" : {}
}

# ----- exceptions -----
class GuildIDNotSetException(Exception):
    pass

class MemberNotInGuildException(Exception):
    pass

def exceptionCheck(member, guild, data):
    member_id = str(member.id)
    guild_id = str(guild.id)

    if guild_id not in data["guild_ids"]:
        raise GuildIDNotSetException

    if member not in guild.members:
        raise MemberNotInGuildException

# ----- adding methods -----
def add_member(member, guild):
    member_id = str(member.id)
    guild_id = str(guild.id)

    data = read_json(TEST_JSON_PATH)

    exceptionCheck(member, guild, data)  # make sure guild has been added and member is in guild

    # if already added return the current data
    members = data["guild_ids"][guild_id]["members"]
    if member_id in members:
        return members[member_id]

    # set the data to blank
    data["guild_ids"][guild_id]["members"][member_id] = MEMBER_INFO_BLANK

    write_json(TEST_JSON_PATH, data)
    return MEMBER_INFO_BLANK


def add_guild(guild):
    guild_id = str(guild.id)

    data = read_json(TEST_JSON_PATH)

    # if guild already added
    if str(guild.id) in data["guild_ids"]:
        return data["guild_ids"][guild_id]

    data["guild_ids"][guild_id] = GUILD_INFO_BLANK

    write_json(TEST_JSON_PATH, data)
    return GUILD_INFO_BLANK


# ----- getters -----
def get_member_info(member, guild):
    member_id = str(member.id)
    guild_id = str(guild.id)

    data = read_json(TEST_JSON_PATH)
    guild_data = read_json(TEST_JSON_PATH, guild_id=guild_id)

    exceptionCheck(member, guild, data) # make sure guild was added and member in guild

    try:
        return guild_data["members"][member_id]
    except:
        # if member not found
        return add_member(member, guild)

# ----- setters -----
def set_member_value(member, guild, new_value=0):
    member_id = str(member.id)
    guild_id = str(guild.id)

    data = read_json(TEST_JSON_PATH)

    exceptionCheck(member, guild, data) # make sure guild was added and member in guild

    try:
        data["guild_ids"][guild_id]["members"][member_id]["member_value"] = int(new_value)
        write_json(TEST_JSON_PATH, data)
    except:
        pass
    return
def add_member_saved_words(member, guild, saved_words_to_add):
    member_id = str(member.id)
    guild_id = str(guild.id)

    data = read_json(TEST_JSON_PATH)
    exceptionCheck(member, guild, data) # make sure guild was added and member in guild
    try:
        data["guild_ids"][guild_id]["members"][member_id]["member_saved_words"].extend(saved_words_to_add)
        write_json(TEST_JSON_PATH, data)
    except:
        pass
    return

def delete_member_saved_words(member, guild, saved_words_to_delete):
    member_id = str(member.id)
    guild_id = str(guild.id)

    data = read_json(TEST_JSON_PATH)
    exceptionCheck(member, guild, data) # make sure guild was added and member in guild

    for saved_word_to_delete in saved_words_to_delete:
        try:
            data["guild_ids"][guild_id]["members"][member_id]["member_saved_words"].remove(saved_word_to_delete)
        except:
            pass

    write_json(TEST_JSON_PATH, data)
    return

