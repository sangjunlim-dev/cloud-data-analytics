# MapReduce

The MapReduce process input from standard input (STDIN) and writing results to standard output (STDOUT).

## Mapper

For example, for word counter

- Iterates over each word in the input.
- Assigns a value of `1` to each word.
- Generates key-value pairs as input for the reducer function.
- Example output: `<key: word, value: 1>`

## Reducer

- Takes key-value pairs from the mapper (e.g., `<key: hello, value: 1>`).
- Aggregates the number of occurrences for each key.
- Outputs the results to STDOUT.

## Hadoop Commands

### 1. Create Directory for Input Files

```bash
hdfs dfs -mkdir -p /path/to/directory
```

### 2. Upload Input Files

```bash
hdfs dfs -put /local/path/to/file /hdfs/path/to/directory
```

### 3. Run MapReduce Job

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -file /local/path/to/mapper.py -mapper 'python3 mapper.py' \
  -file /local/path/to/reducer.py -reducer 'python3 reducer.py' \
  -input /hdfs/path/to/input \
  -output /hdfs/path/to/output
```

### Command Details

- `file`: Specifies the mapper and reducer script files to be uploaded.
- `mapper` / `reducer`: Defines the commands to execute the mapper and reducer scripts (e.g., `python3 mapper.py`).
- `input`: Path to the input directory in HDFS.
- `output`: Path to the output directory in HDFS.