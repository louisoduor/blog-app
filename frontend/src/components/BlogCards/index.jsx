import Prop from "prop-types";
import { BlogCard } from "../BlogCard";

export const BlogCards = ({ blogs, showbuttons }) => {
  return (
    <>
      {blogs.map((value, index) => {
        return (
          <BlogCard
            content={value.content}
            date={value.createdon}
            id={value.id}
            key={index}
            name={value.name}
            tag={value.tag}
            thumbnail={value.thumbnail}
            title={value.title}
            authorid={value.authorid}
            showbuttons={showbuttons}
          />
        );
      })}
    </>
  );
};

BlogCards.propTypes = {
  blogs: Prop.array,
  showbuttons: Prop.bool,
};
