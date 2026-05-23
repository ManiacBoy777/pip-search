pip() {
    local command="$1"
    shift
    
    case "$command" in
        search)
            pip-search-fix "$@"
            ;;
        *)
            command pip "$command" "$@"
            ;;
    esac
}
