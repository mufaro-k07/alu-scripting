#!/usr/bin/env ruby
log = ARGV[0]

matches = log.scan(/from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# matches is an arrays of arrays; we just need to find the first match
if matches.any?
  sender, reciever, flags = matches[0]
  puts "#{sender},#{receiver},#{flags}"
end
