class MyArray
  attr_reader :length

  def initialize
    @length = 0
    @data = {}
  end

  def get(index)
    @data[index]
  end

  def push(item)
    @data[@length] = item
    @length += 1
  end

  def pop
    last_item = @data[@length - 1]
    @data.delete(@length - 1)
    @length -= 1
    return last_item
  end

  def print_all
    str = ""
    @data.each_value do |val|
      str += "#{val} "
    end
    return str
  end

  #this is why some array is O(n)
  #deleting at an index requires for loop in shift_item(index)
  def delete(index)
    item = @data[index]
    shift_item(index)
    @length -= 1
    return item
  end

  def shift_item(index)
    for i in index..length - 1
      @data[i] = @data[i + 1]
    end
  end
end

newArr = MyArray.new
newArr.push("hi")
newArr.push("a")
newArr.push("b")
newArr.push("c")
puts newArr.print_all
puts newArr.length
puts newArr.delete(2)
puts newArr.print_all
puts newArr.length
