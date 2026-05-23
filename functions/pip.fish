function pip
    set command $argv[1]
    set -e argv[1]
    switch "$command"
        case 'search'
            pip-search-fix $argv
        case '*'
            command pip $command $argv
    end
end
